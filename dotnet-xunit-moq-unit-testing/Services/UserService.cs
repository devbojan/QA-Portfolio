using System;
using QaXunitDemo.Interfaces;
using QaXunitDemo.Models;

namespace QaXunitDemo.Services
{
    public class UserService
    {
        private readonly IUserRepository repository;

        public UserService(IUserRepository repository)
        {
            this.repository = repository;
        }

        public string GetUserName(int id)
        {
            var user = repository.GetUserById(id);

            if (user == null)
                throw new Exception("User not found");

            return user.Name;
        }
    }
}