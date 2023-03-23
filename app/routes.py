from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import PhoneForm
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-phone', methods=["GET", "POST"])
def add_phone():
    form = PhoneForm()
    # Check if the form was submitted and is valid
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone_number = form.phone_number.data
        print(first_name, last_name, address, phone_number)
        new_user = User(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number)
        flash(f"{first_name} {last_name} has been added to the phone book", "success")
        return redirect(url_for('index'))
    return render_template('add_phone.html', form=form)