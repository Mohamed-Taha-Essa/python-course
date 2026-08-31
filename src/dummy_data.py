#generate dummy data for the blog app
import os 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()  




from django.contrib.auth.models import User
from blog.models import Post  

from faker import Faker

fake = Faker()

def create_dummy_data(num_users=5, num_posts=20):
    # Create dummy users
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        User.objects.create_user(username=username, email=email, password=password)
        print(f"Created user: {username} ({email})")

    # Create dummy posts
    users = User.objects.all()
    for _ in range(num_posts):
        author = fake.random_element(users)
        title = fake.sentence(nb_words=6)
        body = fake.paragraph(nb_sentences=5)
        slug = fake.slug()
        Post.objects.create(author=author, title=title, body=body, slug=slug)
        print(f"Created post: {title}")
    print(f"Created {num_users} users and {num_posts} posts.")
create_dummy_data()