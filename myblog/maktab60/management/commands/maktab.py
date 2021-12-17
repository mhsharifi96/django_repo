
from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from post.models import Post
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--post_id', nargs='*', type=int)
        parser.add_argument('--status', nargs='?', type=str)
        
        

    def handle(self, *args, **options):
        print('args:', args)
        print('options:', options)
        posts =Post.objects.all()
        for post in posts:
            print(post)
            

            self.stdout.write(self.style.SUCCESS('Successfully worked '))
        self.stdout.write(self.style.ERROR('Successfully worked '))
        