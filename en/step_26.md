## Overlays cycle

This code creates a `cycle`. We use the `next()` function on this cycle when the `next_overlay_btn` is pressed in order to receive the next overlay in the list. A cycle is needed because when the end of the list of overlays is reached, we want to automatically begin again with the first overlay.

```python
all_overlays = cycle(overlays)
```

