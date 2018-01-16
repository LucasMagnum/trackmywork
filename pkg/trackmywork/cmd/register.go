package cmd

import (
    "fmt"
    "strings"
    "github.com/spf13/cobra"
)


func NewRegisterCommand() *cobra.Command {

    cmd := &cobra.Command{
      Use:   "register",
      Short: "Register a task",
      Run: func(cmd *cobra.Command, args []string) {
        fmt.Println("Register command yey!: " + strings.Join(args, " "))
      },
    }

    return cmd
}
