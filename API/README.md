#JSON schemas for all database getters*
*updaters are coming soon (and controllers after r/w is implemented)

This is just a very brief documentation and guide how to use these files.
Proper full and automated documentation is coming in the next two weeks. 

These json files are a formal definition how the json response for all database getters
which could be split in two categories:
- get objects
    - `get_all_rooms`
    - `get_all_bldg_by_name`
    - `get_room_by_name`
    - `get_rooms_by_bldg`
    - `get_sensors_in_room`
- get logs
    - `get_room_logs`
    - `get_all_rooms_logs`
    
Comment if you require additional ones (@FEteam).

It might be more helpful to look at example JSONs (see below) first before diving into all the json schemas.

Specification of parameters to be passed with each request can still be found on the
[Google Docs](https://docs.google.com/document/d/1-XQUulxJPJ9V1QXaj2i28rf5m-onb_xkvA3rmhaJbPU/edit?usp=sharing)
before the full documentation will be ready.

## Example JSONs

Check files `get_objects_esamples.py` and `get_logs_esamples.py`.
They also contain how can the JSONs be validated in Python, see the code,
it is fairly straightforward. 

Thanks to validation of JSONs by their schemas the FEteam can easily fake responses utterly precisely
and hence connecting our systems together should go smoothly.
It will also simplify automatic testing of the database.

## Running on your machine
1. install Python 3
1. clone/pull/copy repo
1. `cd dessertation/DB/API` for Linux, with backslashes for Windows
1. `pip install -r requirements.txt` install dependencies
1. `cd json_schema` this step is important as some of the code relies on the current working directory
(might fix later if it will gain high enough priority)
1. `python3 get_objects_examples.py` prints out and also validates example JSONs for all object getters
1. `python3 get_logs_examples.py` prints out and also validates example JSONs for all log getters
