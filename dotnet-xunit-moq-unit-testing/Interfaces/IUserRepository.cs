using QaXunitDemo.Models;

namespace QaXunitDemo.Interfaces
{
    public interface IUserRepository
    {
        User GetUserById(int id);
    }
}