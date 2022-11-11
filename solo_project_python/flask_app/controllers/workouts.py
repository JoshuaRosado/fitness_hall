from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.workout import Workout
from flask import flash


# =================== HOME PAGE (3)========================================


@app.route("/home")
def home():
    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect("/")
    user = User.get_by_id(session["user_id"])
    workouts = Workout.get_all()
    return render_template("home.html", user=user, workouts=workouts)

# =========================================================================




# @app.route("/workouts/routine")
# def my_workout():
#     if "user_id" not in session:
#         flash("You must be logged in to access the my workouts")
#         return redirect("/")
#     user = User.get_by_id(session["user_id"])
#     workout = Workout.get_all()
    
#     return render_template("view_routine.html", user=user, workout=workout)

# @app.route("/workouts/routine/<int:workout_id>")
# def workouts_page(workout_id):
#     workout = Workout.get_by_id(workout_id)
#     user = User.get_by_id(session["user_id"])
#     return render_template("view_routine.html", workout=workout, user=user)







# ========== Sharing Routine Workout ======================================

@app.route("/share_routine/new")
def create_page():
    user = User.get_by_id(session["user_id"])
    workout = Workout.get_all()


    return render_template("share_routine.html" , user=user, workout=workout)


    
@app.route("/share_routine/", methods=["POST"])
def share_routine():
    valid_workout = Workout.create_workout(request.form)
    if valid_workout:
        return redirect(f'/home')
    return redirect('/share_routine/new')



# =========================================================================



# ========== EDIT and  Update Routine Workout =============================


@app.route("/workout/edit/<int:workout_id>")
def workout_edit_page(workout_id):
    workout = Workout.get_by_id(workout_id)
    user = User.get_by_id(session['user_id'])
    return render_template("edit_workout.html", workout=workout, user=user)




@app.route("/workout/<int:workout_id>", methods=["POST"])
def update_workout(workout_id):

    valid_workout = Workout.update_workout(request.form,session["user_id"])

    if not valid_workout:
        return redirect(f"/workout/edit/{workout_id}/")
        
    return redirect(f"/home")


# ===========================================================================



# ======================== DELETE Routine Workout ===========================

@app.route("/workout/delete/<int:workout_id>")
def delete_by_id(workout_id):
    Workout.delete_routine_by_id(workout_id)
    return redirect("/home")

# ========== Workout Tutorial Page ==========================================

@app.route("/tutorials")
def tutorials():
    user = User.get_by_id(session["user_id"])
    return render_template("tutorials.html", user= user)




# ===========================================================================

#============ View ROUTINE============================
@app.route('/view_routine/<int:workout_id>')
def view_routine(workout_id):
    workout = Workout.get_by_id(workout_id)
    user = User.get_by_id(session["user_id"])
    return render_template("view_routine.html", workout=workout, user=user)