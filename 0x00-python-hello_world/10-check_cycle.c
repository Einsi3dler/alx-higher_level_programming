#include "lists.h"
/**
 * check_cycle - this checks the linked list for circle
 * @list: this is a pointer to the head of the list
 * Return: returns 1 if there is a circle and returns 0 for false
 */
int check_cycle(listint_t *list)
{
	listint_t *Mhead;
	listint_t *Shead;

	Shead = list;
	Mhead = list;

	while (Mhead != NULL)
	{
		int i;

		for (i = 0; i < 3; i++)
		{
			Mhead = Mhead->next;
			if (Mhead == NULL)
			{
				return (0);
			}
		}
		Shead = Shead->next;
		if (Shead == Mhead)
		{
			return (1);
		}

	}
	return (0);
}
