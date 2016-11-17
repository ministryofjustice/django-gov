# -*- coding: utf-8 -*-
from django.test.runner import DiscoverRunner


class GovDiscoverRunner(DiscoverRunner):
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        if not test_labels and 'django_gov' not in test_labels:
            test_labels = ('.', 'django_gov')
        return super(GovDiscoverRunner, self).run_tests(test_labels,
                                                        extra_tests, **kwargs)
