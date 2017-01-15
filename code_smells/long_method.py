# - little methods
#   pros: better explanation, sharing, and choosing
#         good naming can make the code easier to understand(do not need to look into the body)
#   cons: overhead of little methods, readers need to switch context
# - more aggressive about decomposing methods: whenever we need to comment something, extract into
#   a short method explaining the intention instead(method length is not the point, but the
#   explaination of what the method does and how it does it)
# - even a single line of code is worth extracting into a method if it need explanation
# - difficulty: if there are too many parameters and temp variables, it is hard to extract method
#   solution: replace temp with query(to reduce temp variables), and introduce parameter object
#   or preserve whole object(to reduce parameter list)
# - signs of extract method: "comments", "conditionals", or "loops"
#   comments     -> extract into a method with a name explaining the comment
#   conditionals -> decompose conditional
#   loops        -> extract the loop and the code within the loop into its own method
