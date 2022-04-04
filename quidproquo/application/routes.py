from application import app, db
from application.models import Users, Loans, AddProfile, AddDebtDetails
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add_profile', methods=[ 'GET', 'POST'])
def add_profile():
    form = AddProfile()
    if form.validate_on_submit():
        new_profile = Users(user_name=form.user_name.data, password=form.password.data, property=form.property.data, cash=form.cash.data, investments=form.investments.data)
        db.session.add(new_profile)
        db.session.commit()
        return render_template('index.html', message="You have created your profile!")
    else:
        return render_template('add_profile.html', form=form)


@app.route('/add_debt', methods=[ 'GET', 'POST'])
def add_debt():
    form = AddDebtDetails()
    if form.validate_on_submit():
        added_debt = Loans(lender_id=form.lender_id.data, amount_borrowed=form.amount_borrowed.data, amount_paid=form.amount_paid.data)
        db.session.add(added_debt)
        db.session.commit()
        return render_template('index.html', message="Details of debt added!")
    else:
        return render_template('add_debt.html', form=form)


@app.route('/update_debt', methods=[ 'GET', 'POST'])
def update_debt():
    form = AddDebtDetails()
    if form.validate_on_submit:
        updated_debt = Loans(lender_id=form.lender_id.data, amount_borrowed=form.amount_borrowed.data, amount_paid=form.amount_paid.data)
        db.session.add(update_debt)
        db.session.commit()
        return render_template('index.html', message="Details of debt updated!")
    else:
        return render_template('update_debt.html', form=form)


@app.route('/update_profile', methods=[ 'GET', 'POST'])
def update_profile():
    form = AddProfile()
    if form.validate_on_submit:
        update_assets = Users(property=form.property.data, cash=form.cash.data, investments=form.investments.data)
        db.session.add(update_profile)
        db.session.commit()
        return render_template('index.html', message="You updated the value of your assets!")
    else:
        return render_template('update_profile.html', form=form)


@app.route('/delete_debt_entry')
def delete_debt_entry():
    deleted_debt_entry = db.session.query(Loans).filter_by(lender_id=lender_id.first())
    if deleted_debt_entry:
        db.session.delete(deleted_debt_entry)
        db.session.commit()
        return redirect('/home')
    else:
        return redirect('delete_debt_entry')




