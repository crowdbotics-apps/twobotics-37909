from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from apps.models import App, Plan, Subscription

User = get_user_model()
client = APIClient()

class AppServiceTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='mike', email='jacob@example.com', password='top_secret')
        client.force_authenticate(user=self.user)

    def test_app_list(self):
        response = client.get('/api/v1/apps/')
        self.assertEqual(response.status_code, 200)

    def test_create_app(self):
        payload = {
            "name": "My Test App",
            "description": "some descriptions",
            "type": "Web",
            "framework": "Django",
            "domain_name": "www.google.com"
        }
        resp = client.post('/api/v1/apps/', data=payload)
        self.assertEqual(resp.status_code, 201)


    def test_get_app_detail(self):
        new_app = App.objects.create(
            name="My Test App",
            description="some descriptions",
            type="Web",
            framework="Django",
            domain_name="www.google.com",
            user=self.user
        )
        resp = client.get('/api/v1/apps/' + str(new_app.id) + "/")
        self.assertEqual(resp.status_code, 200)

    def test_update_app(self):
        new_app = App.objects.create(
            name="My Test App",
            description="some descriptions",
            type="Web",
            framework="Django",
            domain_name="www.google.com",
            user=self.user
        )

        payload = {
            "name": "My Test App updated",
            "description": "some descriptions",
            "type": "Web",
            "framework": "Django",
            "domain_name": "www.google.com"
        }

        resp = client.put('/api/v1/apps/' + str(new_app.id) + "/", data=payload)
        self.assertEqual(resp.status_code, 200)



class PlanServiceTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='mike', email='jacob@example.com', password='top_secret')
        client.force_authenticate(user=self.user)

    def test_plan_list(self):
        response = client.get('/api/v1/plans/')
        self.assertEqual(response.status_code, 200)


    def test_get_plan_detail(self):
        new_plan = Plan.objects.create(
            name= "Plan A",
            description= "Plan A description",
            price=3.14
        )
        resp = client.get('/api/v1/plans/' + str(new_plan.id) + "/")
        self.assertEqual(resp.status_code, 200)


class SubscriptionTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='mike', email='jacob@example.com', password='top_secret')
        client.force_authenticate(user=self.user)
        self.new_plan = Plan.objects.create(
            name= "Plan A",
            description= "Plan A description",
            price=3.14
        )

        self.new_app = App.objects.create(
            name="My Test App",
            description="some descriptions",
            type="Web",
            framework="Django",
            domain_name="www.google.com",
            user=self.user
        )
    
    def test_subscription_list(self):
        response = client.get('/api/v1/subscriptions/')
        self.assertEqual(response.status_code, 200)

    def test_create_subscription(self):
        payload = {
            "plan": str(self.new_plan.id),
            "app": str(self.new_app.id),
            "active": True
        }
        resp = client.post('/api/v1/subscriptions/', data=payload)
        self.assertEqual(resp.status_code, 201)


    def test_get_subscription_detail(self):
        new_sub = Subscription.objects.create(
            plan= self.new_plan,
            app = self.new_app,
            active=True,
            user=self.user
        )
        resp = client.get('/api/v1/subscriptions/' + str(new_sub.id) + "/")
        self.assertEqual(resp.status_code, 200)

