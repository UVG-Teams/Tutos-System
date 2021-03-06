from django.db import models


class Workflow(models.Model):
    name = models.CharField(
        max_length = 100,
        null = False,
    )

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(
        max_length = 100,
        null = False,
    )
    is_initial = models.BooleanField(
        null = True,
    )
    is_final = models.BooleanField(
        null = True,
    )
    # prev = models.ForeignKey(
    #     'workflows.Status',
    #     null = True,
    #     on_delete = models.SET_NULL,
    #     related_name = 'prev_status',
    # )
    # next = models.ForeignKey(
    #     'workflows.Status',
    #     null = True,
    #     on_delete = models.SET_NULL,
    #     related_name = 'next_status',
    # )
    workflow = models.ForeignKey(
        'workflows.Workflow',
        null = False,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.name