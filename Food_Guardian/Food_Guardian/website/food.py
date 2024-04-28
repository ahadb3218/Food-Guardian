from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import SurplusFoodItem  # Assuming you have a model for surplus food items
from . import db

food = Blueprint('food', __name__)

@food.route('/submit_food', methods=['GET', 'POST'])
def submit_food():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        # You can retrieve other fields from the form

        # Validate the form data as needed

        # Create a new SurplusFoodItem instance
        new_food_item = SurplusFoodItem(name=name, description=description)
        # Add the new food item to the database
        db.session.add(new_food_item)
        db.session.commit()

        flash('Food item submitted successfully!', category='success')
        return redirect(url_for('auth.home'))  # Redirect to appropriate route after submission

    return render_template("submit_food.html")  # Render the form template for submitting surplus food
