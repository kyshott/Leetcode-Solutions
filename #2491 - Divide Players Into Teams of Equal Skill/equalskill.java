class Solution {
    public long dividePlayers(int[] skill) {
        Arrays.sort(skill);

        long total = 0;

        for (int i = 0; i < skill.length / 2; i++) {
            long sum = skill[i] + skill[(skill.length - 1) - i];
            if(sum != skill[0] + skill[skill.length - 1]) {
                return -1;
            }
            total += skill[i] * skill[(skill.length - 1) - i];
        }
        return total;
    }
}
