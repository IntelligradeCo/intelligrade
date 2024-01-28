import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

# Calling make_table function
courses_number = user_selections()
make_table(courses_number)

