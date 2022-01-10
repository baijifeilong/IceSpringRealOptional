# IceSpringRealOptional

**Real** `Optional` type in `python`, not `@Nullable` annotation.

## Official sites

- Home: [https://baijifeilong.github.io/2022/01/09/ice-spring-real-optional/index.html](https://baijifeilong.github.io/2022/01/09/ice-spring-real-optional/index.html)
- Github: [https://github.com/baijifeilong/IceSpringRealOptional](https://github.com/baijifeilong/IceSpringRealOptional)
- PyPI: [https://pypi.org/project/IceSpringRealOptional](https://pypi.org/project/IceSpringRealOptional)

## Features

- All `Java 8` style `Optional` API support
- All `Generic Type` annotation support

## Install

- PyPI: `pip install IceSpringRealOptional`

## Usage

```python
from IceSpringRealOptional.maybe import Maybe

maybe = Maybe.ofNullable("CommonSense")
print("{}: isPresent={}".format(maybe, maybe.isPresent()))
print("{}: value={}".format(maybe, maybe.get()))
maybe.ifPresent(lambda x: print(f"{x} exist"))
print("{}'s length: {}".format(maybe, maybe.map(len)))

empty = Maybe.empty()
print(empty.orElse("{} is empty".format(empty)))
print(empty.orElseGet(lambda: "{} is empty again".format(empty)))

try:
    Maybe.empty().orElseThrow(lambda: RuntimeError("Unlucky"))
except RuntimeError as e:
    print("Runtime error caught: {}".format(e))
```

### Example Output

```
<Maybe:CommonSense>: isPresent=True
<Maybe:CommonSense>: value=CommonSense
CommonSense exist
<Maybe:CommonSense>'s length: <Maybe:11>
<Maybe:None> is empty
<Maybe:None> is empty again
Runtime error caught: Unlucky
```

## License

MIT
