from pathlib import Path
import warnings
class Report:

    @classmethod
    def save_report(cls,path:Path, user:str, time_in:str, time_out:str):
        warnings.warn("This function is experimental")
        """Output pattern from Requirements.pdf"""
        output_str = f"""
# Report \n
|  login    |  time_in  | time_out  |
|-----------|-----------|-----------|
|{user:^11}|{time_in:^11}|{time_out:^11}|


"""
        with open(path/'report.txt', mode="a+", encoding="utf-8") as report:
            report.write(output_str)
        

