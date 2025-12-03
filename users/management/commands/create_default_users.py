from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction


class Command(BaseCommand):
    help = 'Creates default users including a superuser for initial setup'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Create superuser
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@carpool.com',
                    password='sassy',
                    first_name='Admin',
                    last_name='User'
                )
                self.stdout.write(self.style.SUCCESS('✓ Created superuser: admin / admin123'))
            else:
                self.stdout.write(self.style.WARNING('⚠ Superuser "admin" already exists'))

            # Create default test users
            default_users = [
                {
                    'username': 'john',
                    'email': 'john@example.com',
                    'password': 'Root@123',
                    'first_name': 'John',
                    'last_name': 'Doe'
                },
                {
                    'username': 'med',
                    'email': 'med@example.com',
                    'password': 'Root@123',
                    'first_name': 'Jane',
                    'last_name': 'Smith'
                },
                {
                    'username': 'carol',
                    'email': 'carol@example.com',
                    'password': 'Root@123',
                    'first_name': 'carol',
                    'last_name': 'Wilson'
                },
                {
                    'username': 'alice',
                    'email': 'alice@example.com',
                    'password': 'Root@123',
                    'first_name': 'Alice',
                    'last_name': 'Johnson'
                },
            ]

            created_count = 0
            for user_data in default_users:
                if not User.objects.filter(username=user_data['username']).exists():
                    User.objects.create_user(**user_data)
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✓ Created user: {user_data["username"]} / Root@123'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'⚠ User "{user_data["username"]}" already exists'
                        )
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f'\n✅ Setup complete! Created {created_count} new users.'
                )
            )
            self.stdout.write(
                self.style.SUCCESS(
                    '\n📝 Superuser credentials:\n   Username: admin\n   Password: sassy'
                )
            )
            self.stdout.write(
                self.style.SUCCESS(
                    '\n📝 Test user credentials:\n   All test users have password: Root@123'
                )
            )
