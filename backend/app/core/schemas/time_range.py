from datetime import datetime


class TimeRange:
    start: datetime
    end: datetime

    def overlaps(self, other: 'TimeRange'):
        """Test if two ranges overlap"""

        return not (other.end < self.start or other.end < other.start)
