Expensior
=========

Expensior is a self-hosted Django application designed to help individuals log and manage their personal expenses.

Features
--------

*   **User Management**: Register, log in, and manage your profile.
*   **Expense Management**: Add, edit, view, and delete expenses with ease.
*   **Analytics (Planned)**: Get insights into your spending with monthly summaries, category-wise breakdowns, and trends over time.
*   **Responsive Design**: Whether you're on a desktop or mobile, Expensior provides a seamless experience.

Setup
-----

1. **Clone the Repository**

    ```bash
    git clone https://github.com/omerbustun/expensior.git
    ```
    ```bash
    cd expensior
    ```

2. **Set Up a Virtual Environment**

    ```bash
    python -m venv venv
    ```
    ```bash
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**


    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**


    ```bash
    python manage.py runserver
    ```

Visit `http://localhost:8000/` in your browser to access the application.

Development Status
------------------

Expensior is currently in active development. It's not recommended for production use as features might be incomplete or subject to change.

Contribution
------------

If you find a bug or have a feature request, please open an issue. If you'd like to contribute code, open a pull request.

License
-------

Expensior is open-source software, licensed under [GPL-3.0](LICENSE).
