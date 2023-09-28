import csv
import pprint
from typing import List, Iterable, Optional

from presidio_analyzer import BatchAnalyzerEngine, DictAnalyzerResult
from presidio_anonymizer import BatchAnonymizerEngine


class CSVAnalyzer(BatchAnalyzerEngine):

    def analyze_csv(
        self,
        csv_full_path: str,
        language: str,
        keys_to_skip: Optional[List[str]] = None,
        **kwargs,
    ) -> Iterable[DictAnalyzerResult]:

        with open(csv_full_path, 'r') as csv_file:
            csv_list = list(csv.reader(csv_file))
            csv_dict = {header: list(map(str, values)) for header, *values in zip(*csv_list)}
            analyzer_results = self.analyze_dict(csv_dict, language, keys_to_skip)
            return list(analyzer_results)


if __name__ == "__main__":

    analyzer = CSVAnalyzer()
    analyzer_results = analyzer.analyze_csv('/Users/arlenagjackson/Downloads/random_sample_Aran_1_manchester_redaction_annotation.csv',
                                            language="en")
    pprint.pprint(analyzer_results)

    anonymizer = BatchAnonymizerEngine()
    anonymized_results = anonymizer.anonymize_dict(analyzer_results)
    pprint.pprint(anonymized_results)