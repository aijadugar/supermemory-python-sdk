# Settings

Types:

```python
from supermemory.types import SettingUpdateResponse
```

Methods:

- <code title="put /settings">client.settings.<a href="./src/supermemory/resources/settings.py">update</a>(\*\*<a href="src/supermemory/types/setting_update_params.py">params</a>) -> <a href="./src/supermemory/types/setting_update_response.py">SettingUpdateResponse</a></code>

# Memory

Types:

```python
from supermemory.types import (
    MemoryCreateResponse,
    MemoryUpdateResponse,
    MemoryListResponse,
    MemoryDeleteResponse,
)
```

Methods:

- <code title="post /add">client.memory.<a href="./src/supermemory/resources/memory.py">create</a>(\*\*<a href="src/supermemory/types/memory_create_params.py">params</a>) -> <a href="./src/supermemory/types/memory_create_response.py">MemoryCreateResponse</a></code>
- <code title="put /update/{id}">client.memory.<a href="./src/supermemory/resources/memory.py">update</a>(id, \*\*<a href="src/supermemory/types/memory_update_params.py">params</a>) -> <a href="./src/supermemory/types/memory_update_response.py">MemoryUpdateResponse</a></code>
- <code title="get /memories">client.memory.<a href="./src/supermemory/resources/memory.py">list</a>(\*\*<a href="src/supermemory/types/memory_list_params.py">params</a>) -> <a href="./src/supermemory/types/memory_list_response.py">MemoryListResponse</a></code>
- <code title="delete /delete/{id}">client.memory.<a href="./src/supermemory/resources/memory.py">delete</a>(id) -> <a href="./src/supermemory/types/memory_delete_response.py">MemoryDeleteResponse</a></code>
- <code title="get /memory/{id}">client.memory.<a href="./src/supermemory/resources/memory.py">get</a>(id) -> None</code>

# Search

Types:

```python
from supermemory.types import SearchExecuteResponse, SearchFastResponse
```

Methods:

- <code title="post /search">client.search.<a href="./src/supermemory/resources/search.py">execute</a>(\*\*<a href="src/supermemory/types/search_execute_params.py">params</a>) -> <a href="./src/supermemory/types/search_execute_response.py">SearchExecuteResponse</a></code>
- <code title="get /fastsearch">client.search.<a href="./src/supermemory/resources/search.py">fast</a>(\*\*<a href="src/supermemory/types/search_fast_params.py">params</a>) -> <a href="./src/supermemory/types/search_fast_response.py">SearchFastResponse</a></code>

# Connection

Methods:

- <code title="get /connect/{app}">client.connection.<a href="./src/supermemory/resources/connection.py">create</a>(app, \*\*<a href="src/supermemory/types/connection_create_params.py">params</a>) -> None</code>
- <code title="get /connections/{connectionId}">client.connection.<a href="./src/supermemory/resources/connection.py">retrieve</a>(connection_id) -> None</code>
