max_score = 25  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students
import re

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_3_no_tie_scores(test_cases):
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(test_cases, list):
            raise ValueError("test_cases should be a list of dictionaries. Contact your professor.")

        combined_normalized_printed = ''

        # Loop through each test case
        for test_case in test_cases:
            try:
                # Grab the necessary data from the test case dictionary
                inputs = test_case["inputs"]
                #expected_printed_messages = test_case["printed_messages"]
                #invalid_printed_messages = test_case["invalid_printed_messages"]
                
                # case_no_ties = False
                # case_ties = False
                matching_numbers_found = False

                num_repeat_iterations = 50

                # repeat test case 50 times, should have a 99.9999% chance of finding a tie score if it exists.
                for _ in range(num_repeat_iterations):
                    # Load in the student's code and capture output
                    _, captured_output, _ = load_student_code(inputs, test_case)

                    # Split the captured output into lines
                    captured_lines = captured_output.splitlines()
                    
                    # first catch if they ever print out actual tie scores:
                    for line in captured_lines:

                        # ignore the line that has the final season record
                        if 'record' in line:
                            continue

                        numbers = re.findall(r'\d+', line)
    
                        # Convert found numbers to integers
                        numbers = [int(num) for num in numbers]

                        # Check if there are at least 2 numbers and if any two numbers are the same by getting rid of duplicates in a set
                        if len(numbers) > 1 and len(numbers) != len(set(numbers)):
                            matching_numbers_found = True
                            break
                    if matching_numbers_found:
                        break
                        
                assert not matching_numbers_found, format_error_message(
                    custom_message=(f"Your code doesn't prevent tie scores for the home and away teams.\n\n"
                                    f"These scores were generated during your code:.\n\n"
                                    f"{line}\n\n"
                                    f"Make sure you either continue generating the scores when there is a tie until "
                                    f"there is no longer a tie, or you find a way to never generate tie scores to begin with."),
                    test_case=test_case,
                    display_inputs=True,
                )

            except AssertionError:
                raise
            
            except Exception as e:
                # Handle other exceptions
                exception_message_for_students(e, test_case)
    
    # the first AssertionError raises the problem here, this raises it to the main level so the test will stop
    except AssertionError:
        raise

    except Exception as outer_e:
        # Catches any problem in grabbing the test cases
        test_case = {"id_test_case": None}
        exception_message_for_students(outer_e, test_case=test_case) 