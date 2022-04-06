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
        added_debt = Loans(lender_id=form.lender_id.data, amount_borrowed=form.amount_borrowed.data, amount_paid=form.amount_paid.data)
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
            updated_profile.property = form.property.data
            updated_profile.cash = form.cash.data
            updated_profile.investments = form.investments.data
            db.session.commit()
            return render_template('index.html', message="You updated the value of your assets!")
    else:
        return render_template('update_profile.html', form=form)


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




# @app.route('/delete_debt_entry')
# def delete_debt_entry():
#     deleted_debt_entry = db.session.query(Loans)
#     if 
#         db.session.delete(deleted_debt_entry)
#         db.session.commit()
#         return redirect('/home')
#     else:
#         return redirect('delete_debt_entry')




