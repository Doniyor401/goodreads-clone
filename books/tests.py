from django.test import TestCase
from django.urls import reverse
from .models import Book
from users.models import CustomUser


class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))
        self.assertContains(response, "No books found.")

    def test_books_list(self):
        Book.objects.create(title="Book1", description="Description 1", isbn="123123")
        Book.objects.create(title="Book2", description="Description 2", isbn="111111")
        Book.objects.create(title="Book3", description="Description 3", isbn="3333333")

        response = self.client.get(reverse("books:list"))

        books = Book.objects.all()

        for book in books:
            self.assertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(title="Book1", description="Description 1", isbn="123123")

        response = self.client.get(reverse("books:detail", kwargs={"id": book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

    def test_search_books(self):
        book1 = Book.objects.create(title="Sport", description="Description 1", isbn="123123")
        book2 = Book.objects.create(title="Guide", description="Description 2", isbn="111111")
        book3 = Book.objects.create(title="Shoe Dog", description="Description 3", isbn="3333333")

        response = self.client.get(reverse("books:list") + "?q=sport")
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + "?q=guide")
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + "?q=shoe")
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book2.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        book = Book.objects.create(title="Book1", description="Description 1", isbn="123123")

        user = CustomUser.objects.create(
            username="abbos", first_name="Abbos", last_name="Xasanov", email="abbosxasanov@gmail.com"
        )
        user.set_password("somepassword")
        user.save()

        self.client.login(username="abbos", password="somepassword")

        self.client.post(reverse("books:reviews", kwargs={"id": book.id}), data={"stars_given": 3,
                                                                                         "comment": "Nice book"
                                                                                         })
        book_reviews = book.bookreview_set.all()

        self.assertEqual(book_reviews.count(), 1)
        self.assertEqual(book_reviews[0].stars_given, 3)
        self.assertEqual(book_reviews[0].comment, "Nice book")
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)
