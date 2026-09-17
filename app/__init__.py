#===========================================================
# APP NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# Helper Functions
#===========================================================

def get_mb():
    mb = None
    mb_id = session.get("mb", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, socket, ram
            FROM mbs
            WHERE id=?
        """
        params = (mb_id, )
        mb = db.execute(sql, params).fetchone()

    return mb


def get_cpu():
    cpu = None
    cpu_id = session.get("cpu", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, socket
            FROM cpus
            WHERE id=?
        """
        params = (cpu_id, )
        cpu = db.execute(sql, params).fetchone()

    return cpu


def get_ram():
    ram = None
    ram_id = session.get("ram", None)

    with connect_db() as db:
        sql = """
            SELECT id, name
            FROM rams
            WHERE id=?
        """
        params = (ram_id, )
        ram = db.execute(sql, params).fetchone()

    return ram


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Welcome page
#-----------------------------------------------------------
@app.get("/")
def show_welcome():
    # Create empty config in session
    if not session.get("mb"):
        session["mb"]  = None
        session["cpu"] = None
        session["ram"] = None

    mb  = get_mb()
    cpu = get_cpu()
    ram = get_ram()

    return render_template(
        "pages/show_config.jinja",
        mb = mb,
        cpu = cpu,
        ram = ram
    )


#-----------------------------------------------------------
# Config - Pick MB
#-----------------------------------------------------------
@app.get("/config/mb")
def config_pick_mb():

    mb  = get_mb()
    cpu = get_cpu()
    ram = get_ram()

    with connect_db() as db:
        sql = """
            SELECT id, name, socket, ram
            FROM mbs
        """
        params = ()
        mbs = db.execute(sql, params).fetchall()

        return render_template(
            "pages/pick_mb.jinja",
            mb = mb,
            cpu = cpu,
            ram = ram,
            mbs = mbs
        )


#-----------------------------------------------------------
# Config - Process MB
#-----------------------------------------------------------
@app.post("/config/mb")
def config_process_mb():
    mb_id = request.form.get("mb")
    session["mb"] = int(mb_id)
    session["cpu"] = None
    session["ram"] = None

    return redirect("/config/cpu")


#-----------------------------------------------------------
# Config - Pick CPU
#-----------------------------------------------------------
@app.get("/config/cpu")
def config_pick_cpu():

    mb  = get_mb()
    cpu = get_cpu()
    ram = get_ram()

    if not mb:
        flash("Choose a suitable MB first!", "error")
        return redirect("/config/mb")

    with connect_db() as db:
        socket = mb.get("socket")

        sql = """
            SELECT id, name, socket
            FROM cpus
            WHERE socket=?
        """
        params = (socket, )
        cpus = db.execute(sql, params).fetchall()

        return render_template(
            "pages/pick_cpu.jinja",
            mb = mb,
            cpu = cpu,
            ram = ram,
            cpus = cpus
        )


#-----------------------------------------------------------
# Config - Process CPU
#-----------------------------------------------------------
@app.post("/config/cpu")
def config_process_cpu():
    cpu_id = request.form.get("cpu")
    session["cpu"] = int(cpu_id)

    return redirect("/config/ram")


#-----------------------------------------------------------
# Config - Pick RAM
#-----------------------------------------------------------
@app.get("/config/ram")
def config_pick_ram():

    mb  = get_mb()
    cpu = get_cpu()
    ram = get_ram()

    if not mb:
        flash("Choose a suitable MB first!", "error")
        return redirect("/config/mb")

    with connect_db() as db:
        ram = mb.get("ram")

        sql = """
            SELECT id, name, type
            FROM rams
            WHERE type=?
        """
        params = (ram, )
        rams = db.execute(sql, params).fetchall()

        return render_template(
            "pages/pick_ram.jinja",
            mb = mb,
            cpu = cpu,
            ram = ram,
            rams = rams
        )


#-----------------------------------------------------------
# Config - Process RAM
#-----------------------------------------------------------
@app.post("/config/ram")
def config_process_ram():
    ram_id = request.form.get("ram")
    session["ram"] = int(ram_id)

    return redirect("/")


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

