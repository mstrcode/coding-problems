## LEET CODE LINK: https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

from collections import defaultdict, namedtuple
from queue import Queue
from typing  import List
class Solution:
    def BFS(self, graph: dict, start: str, initial_amount: float) -> dict:
        # Keeps track, what is max reach value to a node from the 'start'
        mx_reach = defaultdict(lambda: 0)
        q = Queue()
        q.put((start, initial_amount))

        mx_reach[start] = initial_amount
        # current_amount = initial_amount
        while not q.empty():
            current_node, reach_amount = q.get()
            for neighbour in graph[current_node]:
                if neighbour.rate*reach_amount > mx_reach[neighbour.label]:
                    # calculate amount on reaching neighbout
                    mx_reach[neighbour.label] = neighbour.rate*reach_amount
                    q.put((neighbour.label, neighbour.rate*reach_amount))
        return mx_reach




    # build graph using adjecency list
    def buildGraph(self, pairs: List[List[str]], rates: List[float]) -> dict:
        """
        buildGraph will build the graph based on pairs and rates as pair will become and edge and corresponding rate will become weight, 
        Also the reverse edge will be 1/rate

        Return:
            Adjecency graph
        """
        # pairs = [[1,2], [1,3],[2,4], [3,4]]
        # rates = [1.0, 2.0, 3.0, 2.0]
        # A defaultdictionary that returns by default zero
        adj = defaultdict(lambda: None)
        node = namedtuple('Node', ('label', 'rate'))
        for i, pair in enumerate(pairs):
            from_ = pair[0]; to = pair[1]
            if adj[from_] is None:
                adj[from_] = []

            if adj[to] is None:
                adj[to] = []

            adj[from_].append(node(to, rates[i]))
            adj[to].append(node(from_, 1.0/rates[i]))
        return adj
            

    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        """
        If we know what maximum amount to reach a node on day1 and day2, we can solve this problem
        i.e.
        """
        graph_day1 = self.buildGraph(pairs1, rates1)
        graph_day2 = self.buildGraph(pairs2, rates2)

        # print(graph_day1)
        # We need to chose a currency on which we want to reach having maximum current (say on day1 we reach on intermediate currency)
        # And from there we want to reach back to the initial currency

        # So first we check on day one, what is the maximum currency value on reaching a node
        # starting from initialCurrency
        # mx_reach_d1 currency : max value to read
        mx_reach_d1 = self.BFS(graph=graph_day1, start=initialCurrency, initial_amount=1.0)
        

        max_amount = 0.0
        for intermediate_node, mx in mx_reach_d1.items():
            if graph_day2[intermediate_node] is not None:
                mx_reach_d2 = self.BFS(graph=graph_day2, start=intermediate_node, initial_amount=mx)
                # print(intermediate_node, mx_reach_d2)
                max_amount = max(max_amount, mx_reach_d2[initialCurrency])

        return max(max_amount,1)