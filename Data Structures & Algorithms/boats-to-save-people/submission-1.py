class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # bruteforce:

        # n = len(people)
        # boats = 0
        # for i in range(n):
        #     if people[i] == limit:
        #         boats += 1
        #     for j in range(i, n):
        #         if people[i] + people[j] == limit:
        #             print(people[i], people[j])
        #             boats += 1
        # return boats
# ___________________________________________________

        # two pointer:
        n = len(people)
        boats = 0
        l,r = 0, n-1
        people.sort()
        while l<=r:
            possible_pair = limit - people[r]
            r -= 1
            boats += 1
            if l <= r and possible_pair >= people[l]:
                l+= 1
        return boats