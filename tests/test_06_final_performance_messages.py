max_score = 10  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students, get_similarity_feedback
import re

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_06_final_performance_messages(current_test_name, input_test_cases):
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_input_test_case": None}
            exception_message_for_students(ValueError("input_test_cases should be a list of dictionaries. Contact your professor."), input_test_case, current_test_name) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        final_1, final_2, final_3 = ["qualified for the ncaa soccer tournament", "you had a good season", "your team needs to practice"]
        # Loop through each test case
        for input_test_case in input_test_cases:

            # Grab the necessary data from the test case dictionary
            inputs = input_test_case["inputs"]
            num_repeat_iterations = 50

            final_season_record_regex = re.compile('Final season record.*', re.IGNORECASE)

            for _ in range(num_repeat_iterations):
                # Load in the student's code and capture output
                manager_payload = load_student_code(current_test_name,inputs, input_test_case)
                captured_output = manager_payload.get('captured_output')
                # Split the captured output into lines
                captured_lines = captured_output.splitlines()
                
                normalized_captured_print_statements = [normalize_text(captured_print) for captured_print in captured_lines]
                normalized_captured_print_statements = '\n'.join(normalized_captured_print_statements)

                for line in captured_lines:
                    match = final_season_record_regex.search(line)
                    if match:
                        break

                assert match, format_error_message(
                custom_message=(f"The test couldn't find any printed statement for:\n\n"
                                f"\"Final season record <# wins> - <# losses>\"\n\n"
                                f"If you are printing a message like that, double check your spelling.\n\n"
                                f"ALL YOUR PRINTED OUTPUT:\n"
                                f"------------------------\n"
                                f"Below are all the printed messages from your code (ignoring punctuation / capitalization):\n\n"
                                f"{normalized_captured_print_statements}\n\n"),
                current_test_name=current_test_name,
                input_test_case=input_test_case,
                display_inputs=True,
                )

                final_record_str = match.group()
                numbers = re.findall(r'\d+', final_record_str)
                # Convert found numbers to integers
                numbers = [int(num) for num in numbers]

                assert len(numbers) == 2, format_error_message(
                custom_message=(f"The test couldn't find exactly 2 numbers in the printed statement for:\n\n"
                                f"\"Final season record <# wins> - <# losses>\"\n\n"
                                f"If you are printing a message like that, double check your spelling. Make sure you don't include only 1 number or more than 2. "
                                f"Below are all the printed messages from your code (ignoring punctuation / capitalization):\n\n"
                                f"{normalized_captured_print_statements}\n\n"),
                current_test_name=current_test_name,
                input_test_case=input_test_case,
                display_inputs=True,
                )

                season_record_percent = numbers[0] / sum(numbers)

                if season_record_percent >= .75:
                    final_message = final_1
                elif season_record_percent >= .50:
                    final_message = final_2
                else:
                    final_message = final_3

                
                assert final_message in normalized_captured_print_statements, format_error_message(
                custom_message=(f"In this run, your code produced the final season record of:\n\n"
                                f"{final_record_str}\n\n"
                                f"With {numbers[0]} wins, and {sum(numbers)} total games played (wins + losses). Which implies a "
                                f"{season_record_percent:.2%} win rate. Given that win rate, your code should print out:\n\n"
                                f"{final_message}\n\n"
                                f"But that couldn't be found in your printed output. Double check that you are correctly displaying "
                                f"wins and losses in the \"Final season record\" message, correctly calculating wins and losses, "
                                f"and that your if statements are constructed to correctly print the correct final message. Double check your spelling too.\n\n"
                                f"Below are all the printed messages from your code (ignoring punctuation / capitalization):\n\n"
                                f"{normalized_captured_print_statements}\n\n"),
                current_test_name=current_test_name,
                input_test_case=input_test_case,
                display_inputs=True,
            )

    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case)