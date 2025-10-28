from track.tracker import KevTracker

# Test parsing
def test_tracker_parse():
    tracker = KevTracker()
    items = tracker.new_items()
    assert items is not None

# Test discovering new KEV
def test_tracker_find_new_kev():
    tracker = KevTracker(start_count = 1448)
    items = tracker.new_items()
    assert len(items) >= 1

# Test failure to discover KEV
def test_tracker_fail_find_new_kev():
    tracker = KevTracker(start_count = float('inf'))
    items = tracker.new_items()
    assert items is None