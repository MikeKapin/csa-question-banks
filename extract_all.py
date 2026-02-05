import json
import os

# G2 Exam IDs from the list
g2_exam_ids = [
    "exam_1", "exam_10", "exam_11", "exam_12", "exam_13", "exam_14", "exam_15",
    "exam_16", "exam_17", "exam_18", "exam_19", "exam_2", "exam_20", "exam_21",
    "exam_22", "exam_28", "exam_29", "exam_30", "exam_32", "exam_33", "exam_5",
    "exam_6", "exam_8", "exam_9", "mod_23_forced_air_add_ons_exam", "exam_26",
    "exam_27", "exam_28", "exam_29", "exam_30", "exam_31", "exam_32", "exam_33",
    "exam_34", "exam_35", "exam_36", "exam_37", "exam_38"
]

# G3 Quiz IDs from the list
g3_quiz_ids = [
    "g3_quiz_1", "g3_quiz_2", "g3_quiz_3", "g3_quiz_4", "g3_quiz_5", "g3_quiz_6",
    "g3_quiz_7", "g3_quiz_8", "g3_quiz_9", "g3_quiz_10", "g3_quiz_11", "g3_quiz_12",
    "g3_quiz_13", "g3_quiz_14", "g3_quiz_15", "g3_quiz_16", "g3_quiz_17", "g3_quiz_18",
    "g3_quiz_19", "g3_quiz_20", "g3_exam_prep_21", "g3_exam_prep_22", "g3_exam_prep_23",
    "g3_exam_prep_25", "g3_quiz_25"
]

print(f"Total G2 Exams: {len(g2_exam_ids)}")
print(f"Total G3 Quizzes: {len(g3_quiz_ids)}")

# This script will be used as a reference for manual MCP calls
# Since we can't directly call MCP tools from Python, we'll document the process
