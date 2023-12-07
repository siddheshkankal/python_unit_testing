import random
from unittest.mock import Mock
 
 
techs = ['python', 'sql', 'java', 'aws', 'c++']
 
random.choice = Mock(return_value='aws')
print(random.choice.call_count)
random.choice()
print(random.choice.call_count)


# Alternative solution with patch():

# import random
# from unittest.mock import patch
 
 
# techs = ['python', 'sql', 'java', 'aws', 'c++']
 
# with patch('random.choice', return_value='aws') as mock_choice:
#     print(mock_choice.call_count)
#     random.choice(techs)
#     print(mock_choice.call_count)