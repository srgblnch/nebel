# nebel naming system

**DRAFT**

First of all any distributed system must be based on [uri](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)

```
schema:\[//\[user\[:password]@]host\[:port]]\[/path]\[?query]\[#fragment]
```

* schema: Not (yet) registered the tag for this system is *nebel*. No need for an *s* like *https* because encryption is native (no option for clear text communications).
* *user\[:password]*: When user authentication is required, here is the place. But users will only act in the interface level.
* *host\[:port]*: No single host meaning, this identifies a distributed system. No meaning for port.
* **path**: Name of an element of the distributed system.
* **query**: Attribute sequence (with assignments when write) separated by a delimiter ';' for sequential application, '&' for parallel application.
* **fragment**: (...)

Examples:
* *nebel://test/agent?id*: request an attribute 'id' to an agent in the 'test' distributed system.
** It can be also _nebel://test/ag/en/t?i/d_ where 'agent' has on its name some kind of separators to define a hierarchy.
* *nebel:/agent?id*: request an attribute 'id' to an agent in the distributed system where one lives.
* *nebel:?id*: requests an attribute of the distributed system where one lives.
