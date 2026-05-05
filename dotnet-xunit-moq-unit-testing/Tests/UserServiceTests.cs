using Xunit;
using Moq;
using FluentAssertions;
using System;
using QaXunitDemo.Interfaces;
using QaXunitDemo.Models;
using QaXunitDemo.Services;

namespace QaXunitDemo.Tests
{
    public class UserServiceTests
    {
        private readonly Mock<IUserRepository> mockRepo;
        private readonly UserService userService;

        public UserServiceTests()
        {
            mockRepo = new Mock<IUserRepository>();
            userService = new UserService(mockRepo.Object);
        }

        [Fact]
        public void GetUserName_ValidUser_ReturnsName()
        {
            // Arrange
            mockRepo.Setup(x => x.GetUserById(1))
                    .Returns(new User { Name = "Bojan" });

            // Act
            var result = userService.GetUserName(1);

            // Assert
            result.Should().Be("Bojan");
            mockRepo.Verify(x => x.GetUserById(1), Times.Once);
        }

        [Fact]
        public void GetUserName_UserNotFound_ThrowsException()
        {
            // Arrange
            mockRepo.Setup(x => x.GetUserById(2))
                    .Returns((User)null);

            // Act
            Action act = () => userService.GetUserName(2);

            // Assert
            act.Should().Throw<Exception>()
               .WithMessage("User not found");
        }

        [Fact]
        public void GetUserName_EmptyName_ReturnsEmpty()
        {
            // Arrange
            mockRepo.Setup(x => x.GetUserById(3))
                    .Returns(new User { Name = "" });

            // Act
            var result = userService.GetUserName(3);

            // Assert
            result.Should().BeEmpty();
        }
    }
}