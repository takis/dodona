Schrijf een functie `dict_bmi()` met 1 parameter x. Deze parameter bevat een dictionary met personen met diens gewicht en lengte. De functie heeft een dictionary als return value, met daarin de namen als keys, en als waardes de bmi-waardes.

### Input

Een dictionary met persoonsinformatie.

### Output

Een dictionary met voor persoon diens BMI-waarde.

### Example

**Input:**

      {
            "Jan": {"gewicht": 79, "lengte": 1.89},
            "Piet": {"gewicht": 85, "lengte": 1.80},
      }

**Output:**

      {
            "Jan": 22.1,
            "Piet": 26.2,
      }


### Boilerplate

```python
def dict_bmi(data):
    result = {}
    for naam in data:
        persoon = data[naam]
        gewicht = persoon["gewicht"]
        lengte = ...
        result[naam] = ...
    return result
```