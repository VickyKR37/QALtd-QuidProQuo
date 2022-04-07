from application import app, db
from application.models import Users, Loans, AddProfile, AddDebtDetails
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def home():
    all_users = Users.query.all()
    return render_template('index.html', all_users=all_users)

@app.route('/add_profile', methods=['GET', 'POST'])
def add_profile():
    form = AddProfile()
    if form.validate_on_submit():
        new_profile = Users(user_name=form.user_name.data, password=form.password.data, 
        property=form.property.data, cash=form.cash.data, investments=form.investments.data)
        db.session.add(new_profile)
        db.session.commit()
        return render_template('index.html', message="You have created your profile!")
    else:
        return render_template('add_profile.html', message="Try again", form=form)


@app.route('/add_debt', methods=[ 'GET', 'POST'])
def add_debt():
    form = AddDebtDetails()
    if form.validate_on_submit():
        added_debt = Loans(user_id=form.user_id.data, lender_id=form.lender_id.data, amount_borrowed=form.amount_borrowed.data)
        db.session.add(added_debt)
        db.session.commit()
        return render_template('index.html', message="Details of debt added!")
    else:
        return render_template('add_debt.html', message="Try again", form=form)



@app.route('/update_profile/<int:user_id>', methods=[ 'GET', 'POST'])
def update_profile(user_id):
    form = AddProfile()
    updated_profile = Users.query.filter_by(user_id=user_id).first()
    if request.method == 'POST': 
        if updated_profile:
            if form.property.data:
                updated_profile.property = form.property.data
            if form.cash.data:  
                updated_profile.cash = form.cash.data
            if form.investments.data: 
                updated_profile.investments = form.investments.data
            db.session.commit()
            return render_template('index.html', message="You updated the value of your assets!")
    else:
        return render_template('update_profile.html', form=form)


@app.route('/update_debt/<int:user_id>', methods=[ 'GET', 'POST'])
def update_debt(user_id):
    form = AddDebtDetails()
    updated_debt = Loans.query.filter_by(user_id=user_id).first()
    if request.method == 'POST':
        if updated_debt:
            if form.user_id.data:
                updated_debt.user_id = form.user_id.data
            if form.lender_id.data:
                updated_debt.lender_id = form.lender_id.data
            if form.amount_borrowed.data:
                updated_debt.amount_borrowed = form.amount_borrowed.data
            db.session.commit()
            return render_template('index.html', message="Details of debt updated!")
    else:
        return render_template('update_debt.html', form=form)



@app.route('/view_networth/<int:user_id>')
def view_networth(user_id):
    form1 = Users.query.filter_by(user_id=user_id).first()
    form2 = Loans.query.filter_by(user_id=user_id).first()
    assets = form1.cash + form1.investments + form1.property
    debt = form2.amount_borrowed
    result = assets - debt
    return render_template('view_networth.html', result=result)


@app.route('/delete_profile/<int:user_id>')
def delete_profile(user_id):
    deleted_profile = db.session.query(Users).filter_by(user_id=user_id).first()
    if deleted_profile:
        db.session.delete(deleted_profile)
        db.session.commit()
        return redirect('/home')
    else:
        return redirect('/home')




