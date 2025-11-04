from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Activities
        Activity.objects.create(user=tony.email, activity_type='run', duration=30, date='2025-11-01')
        Activity.objects.create(user=steve.email, activity_type='cycle', duration=45, date='2025-11-02')
        Activity.objects.create(user=bruce.email, activity_type='swim', duration=60, date='2025-11-03')
        Activity.objects.create(user=clark.email, activity_type='fly', duration=120, date='2025-11-04')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=200)
        Leaderboard.objects.create(team='dc', points=180)

        # Workouts
        Workout.objects.create(name='Push Ups', description='Upper body workout', difficulty='easy')
        Workout.objects.create(name='Squats', description='Lower body workout', difficulty='medium')
        Workout.objects.create(name='Plank', description='Core workout', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
