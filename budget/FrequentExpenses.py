import collections
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)
<<<<<<< HEAD
categories, count = zip(*top5)
=======
zip(*top5) = categories, count
>>>>>>> bf9538659159226fac4178dab5458dd7e380d267
