from langchain_community.tools import WikipediaQueryRun, tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.pydantic_v1 import BaseModel, Field
from core_app.models import Lecture
import psycopg2
import os

# use the wikipedia tool from langchain_community
#wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# tools = [wikipedia]

# create custom tools

# important part:
# name, description, args_schema

# class QueryWikiInput(BaseModel):
#     query: str = Field(description="query to look up on wikipedia")

# @tool("query_data_from_wikipedia", args_schema=QueryWikiInput)
# def query_data_from_wikipedia(query: str) -> str:
#     """Get data from wikipedia."""
#     output = WikipediaAPIWrapper().run(query)
#     return output

# tools = [query_data_from_wikipedia]

class QueryInput(BaseModel):
    subject: str = Field(description="subject to look up on table database")
    chapter: str = Field(description="chapter to look up on table database")
    
@tool("query_data_from_db_table", args_schema=QueryInput)
def query_data_from_db_table(subject: str, chapter: str) -> str:
    """Get data from database table."""
    instance_qs = Lecture.objects.filter(subject=subject, chapter=chapter)
    if not instance_qs.exists():
        return "Not Found"
    else:
        instance = instance_qs.first()
        print(instance.content)
        return instance.content
        
tools = [query_data_from_db_table]

