
The SDK can be broken into two parts:
- Components
- Interface

### Components

The SDK parts, located in the components, are the core of 
the SDK. They're the re-usable parts that are used to actually get the data 
from the API and format it for the users. There's two types, the single
resource GET request, and the list GET request, although the single-resource variant 
is practically the same as the list-variant with a limit of 1. It's the most 
general part of the SDK and code be re-used with minimal modifications for 
other APIs.

### Interface

The SDK's interface is, of course, what the user sees. This layer has two purposes. The first is to maximize
usability by hiding the complexity of the underlying parts, by providing strong
type hints so the user knows what to expect, and by focusing on ease of navigation.
The second is to contain the configuration for the underlying parts, for example, 
providing the paths, the resources, and how to create the resources (adapters).
