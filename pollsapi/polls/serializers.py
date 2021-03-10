from rest_framework import serializers

from .models import Poll, Question, Answer, Vote


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'answers']


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['name', 'date_begin', 'date_end', 'description', 'questions']


class VoteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'

    def validate(self, data):
        if not (data.get('custom_answer') or data.get('vote_answers')):
            raise serializers.ValidationError("need an answer")
        return data


class PollVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'name']


class QuestionVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text']


class VoteAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']


class VoteSerializer(serializers.ModelSerializer):
    poll = PollVoteSerializer()
    question = QuestionVoteSerializer()
    vote_answers = VoteAnswersSerializer(many=True)

    class Meta:
        model = Vote
        fields = ['date', 'poll', 'question', 'vote_answers', 'custom_answer']
