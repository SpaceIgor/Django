from django.core.management.base import BaseCommand
from faker import Faker
from app.models import Question as APP

class Command(BaseCommand):
    help = 'Create new question'

    def add_arguments(self, parser):
        parser.add_argument('-q', '--quantity', type=int, default=10)

    def handle(self, *args, **options):
        fake = Faker()

        self.stdout.write('Start inserting questions')
        for _ in range(options['quantity']):
        self.stdout.write('Start inserting questions')
        question = APP()
        question.question_text = fake.sentence().replace(".", "?")
        question.save()

    self.stdout.write(self.style.SUCCESS(f"Successfully generate {options['quantity']} questions"))