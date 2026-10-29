TECHSTORE — მზა Django პროექტი

გაშვების ინსტრუქცია (VS Code / Windows):

1. ZIP ფაილი ამოარქივე ცალკე საქაღალდეში.
2. VS Code-ში გახსენი ამ საქაღალდის შიგნით არსებული TechStore_Ready_Project.
3. გახსენი Terminal > New Terminal.
4. გაუშვი ბრძანებები:

   python -m venv myenv
   .\myenv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

5. ბრაუზერში გახსენი:
   http://127.0.0.1:8000/

პროდუქტების გვერდი:
http://127.0.0.1:8000/products/

შენიშვნა:
ეს პროექტი შეიცავს მზა SVG პროდუქტის ილუსტრაციებს, ამიტომ სურათების ცალკე ძებნა ან ჩამოტვირთვა არ გჭირდება.
თუ PowerShell-მა ვირტუალური გარემოს აქტივაცია დაბლოკა, გაუშვი:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
და შემდეგ ხელახლა გაუშვი:
   .\myenv\Scripts\Activate.ps1
