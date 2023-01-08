from typing import Protocol

from devices import SmartSpeaker


class StatusUpdater(Protocol):
    
    def get_status_update(self) -> str:
        ...
        
def log_updater(to_update: StatusUpdater) -> None:
    status = to_update.get_status_update()
    print(f'Entering into database:\n\t{status}')
    
    
if __name__ == "__main__": 
    """Protocols fascilitate the interface segregation principle, one of the core OOP SOLID principles.
    Protocols provide support for structural subtyping (i.e. structural matching/ duck typing), whereas
    abstract base classes support nominal subtyping (i.e. subtypes must be declared explicitly through
    inheritance). Protocols will not through an error at runtime until a method is used which isn't 
    implemented as expected, i.e. type checking will catch errors, but no error is raised at runtime.
    
    They provide flexibility to work with legacy code, allow interfaces to be defined where they are needed,
    and avoid multiple inheritance, which is always a good thing.
    
    Try commenting out the get_status_update implementation in devices to see that the error is found
    by linting only where the object is used as an expected interface, and not upon creation. If you use
    protocols you might want to use them with a static type checker such as mypy."""
    
    speaker = SmartSpeaker()
    log_updater(to_update=speaker)
        