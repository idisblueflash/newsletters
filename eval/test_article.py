import pytest
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

from criteria import CRITERIA


@pytest.mark.parametrize("name,criteria", CRITERIA, ids=[c[0] for c in CRITERIA])
def test_article_criterion(draft_content, name, criteria):
    test_case = LLMTestCase(
        input=criteria,
        actual_output=draft_content,
    )
    metric = GEval(
        name=name,
        criteria=criteria,
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
        model="gpt-4o",
        threshold=0.5,
    )
    assert_test(test_case, [metric])
