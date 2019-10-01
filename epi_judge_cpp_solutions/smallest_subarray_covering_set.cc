#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"

using std::string;
using std::unordered_map;
using std::unordered_set;
using std::vector;

struct Subarray {
  int start, end;
};

Subarray FindSmallestSubarrayCoveringSet(
    const vector<string> &paragraph, const unordered_set<string> &keywords) {
  unordered_map<string, int> keywords_to_cover;
  for (const string &keyword : keywords) {
    ++keywords_to_cover[keyword];
  }

  Subarray result = Subarray{-1, -1};
  int remaining_to_cover = size(keywords);
  for (int left = 0, right = 0; right < size(paragraph); ++right) {
    if (keywords.count(paragraph[right]) &&
        --keywords_to_cover[paragraph[right]] >= 0) {
      --remaining_to_cover;
    }

    // Keeps advancing left until keywords_to_cover does not contain all
    // keywords.
    while (remaining_to_cover == 0) {
      if ((result.start == -1 && result.end == -1) ||
          right - left < result.end - result.start) {
        result = {left, right};
      }
      if (keywords.count(paragraph[left]) &&
          ++keywords_to_cover[paragraph[left]] > 0) {
        ++remaining_to_cover;
      }
      ++left;
    }
  }
  return result;
}

int FindSmallestSubarrayCoveringSetWrapper(
    TimedExecutor &executor, const vector<string> &paragraph,
    const unordered_set<string> &keywords) {
  unordered_set<string> copy = keywords;

  auto result = executor.Run(
      [&] { return FindSmallestSubarrayCoveringSet(paragraph, keywords); });

  if (result.start < 0 || result.start >= paragraph.size() || result.end < 0 ||
      result.end >= paragraph.size() || result.start > result.end) {
    throw TestFailure("Index out of range");
  }

  for (int i = result.start; i <= result.end; i++) {
    copy.erase(paragraph[i]);
  }

  if (!copy.empty()) {
    throw TestFailure("Not all keywords are in the range");
  }

  return result.end - result.start + 1;
}

// clang-format off


int main(int argc, char* argv[]) {
  std::vector<std::string> args {argv + 1, argv + argc};
  std::vector<std::string> param_names {"executor", "paragraph", "keywords"};
  return GenericTestMain(args, "smallest_subarray_covering_set.cc", "smallest_subarray_covering_set.tsv", &FindSmallestSubarrayCoveringSetWrapper, DefaultComparator{}, param_names);
}
// clang-format on
