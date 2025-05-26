# regular courses
from .evaluation_comp1001 import comp1001
from .evaluation_comp1021 import comp1021
from .evaluation_comp1022p import comp1022p
from .evaluation_comp1022q import comp1022q
from .evaluation_comp2011 import comp2011
from .evaluation_comp2012 import comp2012
from .evaluation_comp2611 import comp2611
from .evaluation_comp3111 import comp3111
from .evaluation_comp3511 import comp3511
from .evaluation_comp4511 import comp4511

# bridging courses
from .evaluation_comp1029c import comp1029c
from .evaluation_comp1029j import comp1029j
from .evaluation_comp1029p import comp1029p

overall_evaluation_rating = "1472,1227,576,94,50"

evaluation = [
    comp3511,
    comp2011,
    comp1021,
    comp1022q,
    comp4511,
    comp3111,
    comp2611,
    comp1001,
    comp2012,
    comp1022p,
]

count_evaluation_courses = len(evaluation)
count_evaluation_reports = 0
for item in evaluation:
    count_evaluation_reports += len(item['reports'])




evaluation_bridging = [
    comp1029p,
    comp1029c,
    comp1029j,
]

count_evaluation_bridging_courses = len(evaluation_bridging)
count_evaluation_bridging_reports = 0
for item in evaluation_bridging:
    count_evaluation_bridging_reports += len(item['reports'])






