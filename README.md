# IceSpringRealOptional

**Real** `Optional` type in `python`, not `@Nullable` annotation.

## Official sites

- Home: [https://baijifeilong.github.io/2022/01/09/ice-spring-real-optional/index.html](https://baijifeilong.github.io/2022/01/08/ice-spring-real-optional/index.html)
- Github: [https://github.com/baijifeilong/IceSpringRealOptional](https://github.com/baijifeilong/IceSpringRealOptional)
- PyPI: [https://pypi.org/project/IceSpringRealOptional](https://pypi.org/project/IceSpringRealOptional)

## Features

- All `Java 8` style `Optional` API support
- All `Generic Type` annotation support

## Install

- PyPI: `pip install IceSpringRealOptional`

## Usage

```python
from IceSpringRealOptional import Option

option = Option.ofNullable("CommonSense")
print("{}: isPresent={}".format(option, option.isPresent()))
print("{}: value={}".format(option, option.get()))
option.ifPresent(lambda x: print(f"{x} exist"))
print("{}'s length: {}".format(option, option.map(len)))

empty = Option.empty()
print(empty.orElse("{} is empty".format(empty)))
print(empty.orElseGet(lambda: "{} is empty again".format(empty)))

try:
    Option.empty().orElseThrow(lambda: RuntimeError("Unlucky"))
except RuntimeError as e:
    print("Runtime error caught: {}".format(e))
```

### Example Output

```
<Option:CommonSense>: isPresent=True
<Option:CommonSense>: value=CommonSense
CommonSense exist
<Option:CommonSense>'s length: <Option:11>
<Option:None> is empty
<Option:None> is empty again
Runtime error caught: Unlucky
```

## License

MIT
