from mcp_eval import task, setup, Expect
from mcp_eval.session import TestAgent

@setup
def _cfg():
    pass

@task("basic_website_fetch")
async def basic_website_fetch(agent: TestAgent, session):
    response = await agent.generate_str("Please fetch the content from https://example.com and tell me what you find")
    await session.assert_that(Expect.tools.was_called("fetch", min_times=1))
    # await session.assert_that(Expect.tools.called_with("fetch", {'url': 'https://example.com'}))
    # await session.assert_that(Expect.content.contains("example", case_sensitive=False), response=response)
    # await session.assert_that(Expect.judge.llm("Response indicates successful fetch and describes website content", min_score=0.7), response=response)
    # await session.assert_that(Expect.content.contains("example.com", case_sensitive=False), response=response)
    # await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='Example Domain', field_path=None, match_type="contains", case_sensitive=False, call_index=-1))
    # await session.assert_that(Expect.content.contains("internet access", case_sensitive=False), response=response)
    # await session.assert_that(Expect.performance.max_iterations(3))
    # await session.assert_that(Expect.performance.response_time_under(10000.0))
    # await session.assert_that(Expect.judge.llm("The response should acknowledge that the assistant now has internet access and provide a clear summary of what was found on the example.com website, including its basic purpose as a domain example page.", min_score=0.7), response=response)

# @task("fetch_with_length_limit")
# async def fetch_with_length_limit(agent: TestAgent, session):
#     response = await agent.generate_str("Fetch https://httpbin.org/html but only get the first 1000 characters")
#     await session.assert_that(Expect.tools.was_called("fetch", min_times=1))
#     await session.assert_that(Expect.tools.called_with("fetch", {'url': 'https://httpbin.org/html', 'max_length': 1000}))
#     await session.assert_that(Expect.judge.llm("Response acknowledges length limitation and shows truncated content", min_score=0.7), response=response)
#     await session.assert_that(Expect.content.contains("1000 characters", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("httpbin.org", case_sensitive=False), response=response)
#     await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='<!DOCTYPE html>', field_path=None, match_type="contains", case_sensitive=False, call_index=-1))
#     await session.assert_that(Expect.performance.max_iterations(2))
#     await session.assert_that(Expect.performance.response_time_under(8000.0))
#     await session.assert_that(Expect.judge.llm("The response should correctly use the max_length parameter set to 1000, acknowledge the character limit constraint, and provide a summary of the fetched content from httpbin.org/html that respects the length limitation.", min_score=0.8), response=response)

# @task("raw_html_fetch")
# async def raw_html_fetch(agent: TestAgent, session):
#     response = await agent.generate_str("I need the raw HTML source code of https://httpbin.org/html without any markdown conversion")
#     await session.assert_that(Expect.tools.was_called("fetch", min_times=1))
#     await session.assert_that(Expect.tools.called_with("fetch", {'url': 'https://httpbin.org/html', 'raw': True}))
#     await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='<html>', field_path=None, match_type="contains", case_sensitive=False, call_index=-1))
#     await session.assert_that(Expect.content.contains("\u003c!DOCTYPE html\u003e", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("raw HTML", case_sensitive=False), response=response)
#     await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='<!DOCTYPE html>', field_path=None, match_type="starts_with", case_sensitive=False, call_index=-1))
#     await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='</html>', field_path=None, match_type="contains", case_sensitive=False, call_index=-1))
#     await session.assert_that(Expect.content.contains("\u003c", case_sensitive=True), response=response)
#     await session.assert_that(Expect.content.contains("\u003e", case_sensitive=True), response=response)
#     await session.assert_that(Expect.performance.max_iterations(2))
#     await session.assert_that(Expect.performance.response_time_under(8000.0))
#     await session.assert_that(Expect.judge.llm("The response should correctly use the raw=true parameter to fetch unprocessed HTML source code, present the actual HTML tags and structure without markdown formatting, and acknowledge that raw HTML was requested and delivered.", min_score=0.8), response=response)

# @task("paginated_content_fetch")
# async def paginated_content_fetch(agent: TestAgent, session):
#     response = await agent.generate_str("Fetch https://httpbin.org/html starting from character 500 onwards")
#     await session.assert_that(Expect.tools.was_called("fetch", min_times=1))
#     await session.assert_that(Expect.tools.called_with("fetch", {'url': 'https://httpbin.org/html', 'start_index': 500}))
#     await session.assert_that(Expect.judge.llm("Response indicates content was fetched starting from specified position", min_score=0.7), response=response)
#     await session.assert_that(Expect.content.contains("character 500", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("starting from", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("httpbin.org", case_sensitive=False), response=response)
#     await session.assert_that(Expect.performance.max_iterations(2))
#     await session.assert_that(Expect.performance.response_time_under(8000.0))
#     await session.assert_that(Expect.judge.llm("The response should correctly use the start_index parameter set to 500 to fetch content starting from character position 500, acknowledge the pagination/offset request, and show content that would appear after the first 500 characters of the page.", min_score=0.8), response=response)

# @task("json_api_fetch")
# async def json_api_fetch(agent: TestAgent, session):
#     response = await agent.generate_str("Get the current data from https://httpbin.org/json and explain what it contains")
#     await session.assert_that(Expect.tools.was_called("fetch", min_times=1))
#     await session.assert_that(Expect.tools.called_with("fetch", {'url': 'https://httpbin.org/json'}))
#     await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='slideshow', field_path=None, match_type="contains", case_sensitive=False, call_index=-1))
#     await session.assert_that(Expect.judge.llm("Response successfully parses and explains the JSON data structure", min_score=0.8), response=response)
#     await session.assert_that(Expect.content.contains("JSON", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("contains", case_sensitive=False), response=response)
#     await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='{', field_path=None, match_type="starts_with", case_sensitive=True, call_index=-1))
#     await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='}', field_path=None, match_type="ends_with", case_sensitive=True, call_index=-1))
#     await session.assert_that(Expect.content.contains("slideshow", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("slides", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("httpbin.org", case_sensitive=False), response=response)
#     await session.assert_that(Expect.performance.max_iterations(2))
#     await session.assert_that(Expect.performance.response_time_under(8000.0))
#     await session.assert_that(Expect.judge.llm("The response should successfully fetch JSON data from httpbin.org/json, identify it as JSON format, and provide a clear explanation of the JSON structure and content, including details about the slideshow data structure it typically contains.", min_score=0.8), response=response)

# @task("multiple_url_comparison")
# async def multiple_url_comparison(agent: TestAgent, session):
#     response = await agent.generate_str("Compare the content between https://httpbin.org/html and https://example.com")
#     await session.assert_that(Expect.tools.was_called("fetch", min_times=2))
#     await session.assert_that(Expect.tools.sequence(["fetch", "fetch"], allow_other_calls=False))
#     await session.assert_that(Expect.judge.llm("Response compares content from both websites and highlights differences", min_score=0.8), response=response)
#     await session.assert_that(Expect.content.contains("comparison", case_sensitive=False), response=response)
#     await session.assert_that(Expect.tools.called_with("fetch", {'url': 'https://httpbin.org/html'}))
#     await session.assert_that(Expect.tools.called_with("fetch", {'url': 'https://example.com'}))
#     await session.assert_that(Expect.content.contains("compare", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("httpbin.org", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("example.com", case_sensitive=False), response=response)
#     await session.assert_that(Expect.content.contains("difference", case_sensitive=False), response=response)
#     await session.assert_that(Expect.tools.output_matches(tool_name="fetch", expected_output='Example Domain', field_path=None, match_type="contains", case_sensitive=False, call_index=1))
#     await session.assert_that(Expect.performance.max_iterations(4))
#     await session.assert_that(Expect.performance.response_time_under(15000.0))
#     await session.assert_that(Expect.judge.llm("The response should fetch both URLs sequentially, provide content from both httpbin.org/html and example.com, and offer a meaningful comparison highlighting the differences between the two websites\u0027 content, structure, or purpose.", min_score=0.8), response=response)


