class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Map<Character, Integer>, List<String>> groupByIndex = new HashMap<>();
        for (String str : strs) {
            Map<Character, Integer> charFreqs = new HashMap<>();
            for (char c : str.toCharArray()) charFreqs.put(c, charFreqs.getOrDefault(c, 0) + 1);
            List<String> group = groupByIndex.getOrDefault(charFreqs, new ArrayList<>());
            group.add(str);
            groupByIndex.put(charFreqs, group);
        }
        return new ArrayList<>(groupByIndex.values());
    }
}
